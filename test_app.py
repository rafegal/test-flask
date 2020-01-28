from unittest import mock, TestCase
from app import web_app

class TestTech(TestCase):
    """
        Aqui é feito os testes da camada CRUD.
    """

    def setUp(self):
        self.client = web_app.test_client()


    def test_get_tech_pelo_nome_da_tecnologia_retorna_status_200(self):
        response = self.client.get('/tech/python')
        self.assertEqual(200, response.status_code)

    
    def test_get_tech_pelo_nome_retorna_um_json(self):
        response = self.client.get('/tech/python')
        self.assertEqual('application/json', response.content_type)

    @mock.patch('app.create_tech_db')
    def test_create_tech_retorna_status_201(self, mock_db):
        tech = {'nome': 'Python', 'descricao': 'Linguagem que mais cresce no mundo'}
        response = self.client.post('/tech', json=tech)
        self.assertEqual(201, response.status_code)

    @mock.patch('app.create_tech_db')
    def test_create_tech_retorna_contet_json(self, mock_db):
        tech = {'nome': 'Java', 'descricao': 'Linguagem que mais cresce no mundo'}
        response = self.client.post('/tech', json=tech)
        self.assertEqual('application/json', response.content_type)

    @mock.patch('app.create_tech_db')
    def test_verificar_se_funcao_criacao_banco_de_dados_e_chamada(self,mock_db):
        tech = {'nome': 'Python', 'descricao': 'Linguagem que mais cresce no mundo'}
        response = self.client.post('/tech', json=tech)
        mock_db.assert_called()
    

