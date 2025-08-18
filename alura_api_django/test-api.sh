# arquivo: test-api.sh

echo "--- Requisição GET ---"
curl -X GET https://jsonplaceholder.typicode.com/posts/1
echo "" # Adiciona uma linha em branco

echo "--- Requisição POST ---"
curl -X POST https://jsonplaceholder.typicode.com/posts \
     -H "Content-Type: application/json" \
     -d '{"title":"foo","body":"bar","userId":1}'
echo "" # Adiciona uma linha em branco

echo "--- Requisição POST na minha API ---"
curl -X POST http://127.0.0.1:8000/alunos/ \
     -H "Content-Type: application/json" \
     -d '{"nome": "Maria", "email": "joao@email.com", "cpf": "33333333333", "data_nascimento": "2025-08-18", "celular": "9999999999999"}'
echo ""

echo "--- Requisição GET na minha API ---"
curl -X GET http://127.0.0.1:8000/alunos/1/
echo ""

echo "--- Requisição GET na minha API ---"
curl -X GET http://127.0.0.1:8000/aluno/1/matriculas/
curl -X GET http://127.0.0.1:8000/curso/1/matriculas/
echo ""