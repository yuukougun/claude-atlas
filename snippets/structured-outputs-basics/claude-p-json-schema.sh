claude -p "このリポジトリの README を読み、題名と対象読者を答えて" \
  --output-format json \
  --json-schema '{
    "type": "object",
    "properties": {
      "title": { "type": "string" },
      "audience": { "type": "string" }
    },
    "required": ["title", "audience"],
    "additionalProperties": false
  }'
