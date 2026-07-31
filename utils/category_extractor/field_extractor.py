import csv
import json
import shutil
from pathlib import Path


class FieldExtractor:

    def __init__(self,
                 input_dir="Divar_filters",
                 output_dir="Parsed_filters"):

        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self):

        for json_file in self.input_dir.glob("*.json"):
            self.extract_file(json_file)

    def extract_file(self, json_file):

        print(f"Processing {json_file.name}")

        category_name = json_file.stem

        category_dir = self.output_dir / category_name
        category_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy2(json_file, category_dir / "raw.json")

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        widgets = data.get("page", {}).get("widget_list", [])

        schema = {
            "category": category_name,
            "filters": {}
        }

        rows = []

        for widget in widgets:

            widget_type = widget.get("widget_type")

            uid = widget.get("uid")

            d = widget.get("data", {})

            field = d.get("field", {})

            field_key = field.get("key")

            if not field_key:
                continue

            field_type = field.get("type")

            title = (
                d.get("title")
                or d.get("filter_page_title")
                or d.get("bottom_sheet_title")
                or ""
            )

            placeholder = d.get("placeholder", "")

            options = d.get("options", [])

            schema["filters"][field_key] = {
                "widget_type": widget_type,
                "uid": uid,
                "field_type": field_type,
                "title": title,
                "placeholder": placeholder,
                "data": d
            }

            if options:

                for option in options:

                    rows.append({
                        "field": field_key,
                        "widget_type": widget_type,
                        "field_type": field_type,
                        "title": title,
                        "option_key": option.get("key") or option.get("value"),
                        "option_title": option.get("title") or option.get("display"),
                        "search_keywords": option.get("search_keywords", "")
                    })

            else:

                rows.append({
                    "field": field_key,
                    "widget_type": widget_type,
                    "field_type": field_type,
                    "title": title,
                    "option_key": "",
                    "option_title": "",
                    "search_keywords": ""
                })

        with open(category_dir / "schema.json",
                  "w",
                  encoding="utf-8") as f:

            json.dump(
                schema,
                f,
                ensure_ascii=False,
                indent=4
            )

        if rows:

            with open(category_dir / "filters.csv",
                      "w",
                      newline="",
                      encoding="utf-8-sig") as f:

                writer = csv.DictWriter(
                    f,
                    fieldnames=rows[0].keys()
                )

                writer.writeheader()
                writer.writerows(rows)