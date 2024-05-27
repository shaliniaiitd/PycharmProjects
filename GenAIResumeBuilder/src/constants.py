class Config:
    AZURE_OPENAI_ENDPOINT = "https://ai-proxy.lab.epam.com"
    AZURE_CHAT_DEPLOYMENT_NAME = "gpt-35-turbo-16k"
    AZURE_OPENAI_API_VERSION = "2023-03-15-preview"
    AZURE_OPENAI_API_KEY ="sSZd5Q9IoKB3v8A2IUcET3BlbkFJop19hI3ykBC50Z107JV7"

    TEMPERATURE = 0
    MAX_TOKENS = 60
    TOP_P = 1
    FREQUENCY_PENALTY = 0
    PRESENCE_PENALTY = 0

    ALLOWED_EXTENSIONS = {"docx", "pdf", "jpeg", "jpg", "doc"}

    TEMPLATE_PATH = "static/epam_template.docx"
    OUTPUT_FOLDER = "output"
    UPLOAD_FOLDER = "uploads"

    HEADING_LINE_SPACING = 1.5
    HEADING_FONT_BOLD = True
    HEADING_FONT_NAME = "Arial Black"
    HEADING_FONT_SIZE = 12
    HEADING_FONT_COLOR = (71, 71, 255)
    HEADING_INDENT_LEVEL = 0
    BODY_LINE_SPACING = 1.5
    BODY_INDENT_LEVEL = 12
    BODY_FONT_BOLD = False
    BODY_FONT_NAME = "Trebuchet MS"
    BODY_FONT_SIZE = 10
    BODY_FONT_COLOR = (0, 0, 0)