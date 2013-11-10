import unittest
import por_extenso
from por_extenso import valor_por_extenso_de
        
class TestPorExtenso(unittest.TestCase):
    def test_1_por_extenso_eh_um(self):
        self.assertEqual('um real', valor_por_extenso_de(1.00))
        
    def test_13_por_extenso_eh_treze(self):
        self.assertEqual('treze reais', valor_por_extenso_de(13.00))

    def test_20_por_extenso_eh_vinte(self):
        self.assertEqual('vinte reais', valor_por_extenso_de(20.00))
        
    def test_21_por_extenso_eh_vinte_e_um(self):
        self.assertEqual('vinte e um reais', valor_por_extenso_de(21.00))
        
    def test_100_por_extenso_eh_cem(self):
        self.assertEqual('cem reais', valor_por_extenso_de(100.00))

    def test_102_por_extenso_eh_cento_e_dois(self):
        self.assertEqual('cento e dois reais', valor_por_extenso_de(102.00))
        
    def test_1000_por_extenso_eh_mil(self):
        self.assertEqual('mil reais', valor_por_extenso_de(1000.00))
        
    def test_1001_por_extenso_eh_mil_e_um(self):
        self.assertEqual('mil e um reais', valor_por_extenso_de(1001.00))
        
    def test_1351_por_extenso_eh_mil_trezentos_e_cinquenta_e_um(self):
        self.assertEqual('mil e trezentos e cinquenta e um reais', valor_por_extenso_de(1351.00))
        
    def test_19000_por_extenso_eh_dezenove_mil(self):
        self.assertEqual('dezenove mil reais', valor_por_extenso_de(19000.00))

    def test_100000_por_extenso_eh_cem_mil(self):
        self.assertEqual('cem mil reais', valor_por_extenso_de(100000.00))

    def test_1268351_por_extenso_eh_um_milhao_duzentos_e_sessenta_e_oito_mil_trezentos_e_cinquenta_e_um(self):
        self.assertEqual('um milhao, duzentos e sessenta e oito mil e trezentos e cinquenta e um reais', 
                         valor_por_extenso_de(1268351.00))
        
    def test_1020000_por_extenso_eh_um_milhao_e_vinte_mil(self):
        self.assertEqual('um milhao e vinte mil reais', valor_por_extenso_de(1020000.00))
        
    def test_10000009_por_extenso_eh_dez_milhoes_e_nove(self):
        self.assertEqual('dez milhoes e nove reais', valor_por_extenso_de(10000009.00))

    def test_1_000_030_017_por_extenso_eh_um_bilhao_trinta_mil_e_dezessete(self):
        self.assertEqual('um bilhao, trinta mil e dezessete reais', valor_por_extenso_de(1000030017.00))

    def test_11_000_000_000_por_extenso_eh_onze_bilhoes(self):
        self.assertEqual('onze bilhoes de reais', valor_por_extenso_de(11000000000.00))
        
    def test_15_477_583_696_por_extenso_eh_muito_dinheiro(self):
        self.assertEqual('quinze bilhoes, quatrocentos e setenta e sete milhoes, quinhentos e oitenta e tres mil e seiscentos e noventa e seis reais', 
                         valor_por_extenso_de(15477583696.00))

    def test_4_015_477_583_696_por_extenso_eh_muito_dinheiro(self):
        self.assertEqual('quatro trilhoes, quinze bilhoes, quatrocentos e setenta e sete milhoes, quinhentos e oitenta e tres mil e seiscentos e noventa e seis reais', 
                         valor_por_extenso_de('4015477583696.00'))
                         
    # e os centavos!
    
    def test_um_real_e_um_centavo(self):
        self.assertEqual('um real e um centavo', valor_por_extenso_de(1.01))
     
    def test_um_real_e_quatro_centavos(self):
        self.assertEqual('um real e quatro centavos', valor_por_extenso_de(1.04))

     
unittest.main()