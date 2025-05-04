from parser.xml_parser import Parser
from parser.xml_generator import XMLGenerator

INPUT_PATH = "input/impulse_test_input.xml"
OUTPUT_PATH = "out/config.xml"

def main():
    parser = Parser(INPUT_PATH)
    parser.parse()
    models = parser.get_models()
    root_model = next((m for m in models if m.name == "BTS"), None)
    if root_model:
        generator = XMLGenerator(root_model)
        generator.save_to_file(OUTPUT_PATH)
        print(f"XML создан: {OUTPUT_PATH}")
    else:
        print("Корневая модель не найдена.")

if __name__ == "__main__":
    main()
