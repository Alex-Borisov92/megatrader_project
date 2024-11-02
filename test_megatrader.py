import pytest
import subprocess
import sys
import os

# Получаем абсолютный путь к файлу main.py
SCRIPT_PATH = os.path.abspath('main.py')

# Список тестовых случаев
test_cases = [
    ('input1.txt', 'output1.txt'),
    ('input2.txt', 'output2.txt'),
    ('input3.txt', 'output3.txt'),
    ('input4.txt', 'output4.txt'),
    ('input5.txt', 'output5.txt'),
    ('input6.txt', 'output6.txt'),
    ('input7.txt', 'output7.txt'),
    ('input8.txt', 'output8.txt'),
    ('input9.txt', 'output9.txt'),
    ('input10.txt', 'output10.txt'),
]

@pytest.mark.parametrize("input_file, expected_output_file", test_cases)
def test_megatrader(input_file, expected_output_file):
    # Путь к файлам входных и ожидаемых выходных данных
    input_path = os.path.join('examples', input_file)
    expected_output_path = os.path.join('examples', expected_output_file)

    # Открываем входной файл
    with open(input_path, 'r') as infile:
        # Запускаем скрипт main.py как отдельный процесс
        result = subprocess.run(
            [sys.executable, SCRIPT_PATH],
            stdin=infile,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

    # Читаем ожидаемый вывод
    with open(expected_output_path, 'r') as expected_file:
        expected_output = expected_file.read().strip()

    # Получаем фактический вывод
    actual_output = result.stdout.strip()

    # Проверяем, что вывод соответствует ожидаемому
    assert actual_output == expected_output, f"Test failed for {input_file}"

    # Дополнительно можно проверить, что ошибок не было
    assert result.stderr == '', f"Errors occurred during execution of {input_file}"
