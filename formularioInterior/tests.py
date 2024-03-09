# No arquivo tests.py

import unittest
from django.test import TestCase
from .models import Pessoa 

class PessoaTestCase(TestCase):

    def setUp(self):
        Pessoa.objects.create(nome="Exemplo Pessoa", cpf="123.456.789-00")

    def test_pessoa_nome(self):
        pessoa = Pessoa.objects.get(nome="Exemplo Pessoa")
        self.assertEqual(pessoa.nome, "Exemplo Pessoa")

    def test_pessoa_cpf(self):
        pessoa = Pessoa.objects.get(cpf="123.456.789-00")
        self.assertEqual(pessoa.cpf, "123.456.789-00")

if __name__ == '__main__':
    unittest.main()
