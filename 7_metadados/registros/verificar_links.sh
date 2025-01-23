#!/bin/bash

# Script para verificação de links em arquivos markdown
echo "Iniciando verificação de links..."
echo "Data: $(date)" > links_report.txt

while IFS= read -r file; do
    echo "Verificando: $file" >> links_report.txt
    grep -o "\[.*\](.*)" "$file" >> links_report.txt
    echo "-------------------" >> links_report.txt
done < links_to_check.txt

echo "Verificação concluída. Verifique links_report.txt para resultados." 