import unittest
import cesar


pairs: dict[int, str] = {
    7: "Aab vinder guld igen",
    16: "Programmering er sjovt",
    4: "H5PD rejser sig, når Per kommer ind af døren",
}


class TestCesar(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(cesar.crypt(7, "Aab vinder guld igen"), 'HHI CPUKLY NBSK PNLU')
        self.assertEqual(cesar.crypt(16, "Programmering er sjovt"), 'FHEWHQCCUHYDW UH IZELJ')
        self.assertEqual(cesar.crypt(4, "H5PD rejser sig, når Per kommer ind af døren"), 'LTH VINWIV WMK RV TIV OSQQIV MRH EJ HVIR')

    def test_decrypt(self):
        self.assertEqual(cesar.crypt(-7, cesar.crypt(7, "Aab vinder guld igen")), 'AAB VINDER GULD IGEN')
        self.assertEqual(cesar.crypt(-16, cesar.crypt(16, "Programmering er sjovt")), 'PROGRAMMERING ER SJOVT')
        self.assertEqual(cesar.crypt(-4, cesar.crypt(4, "H5PD rejser sig, når Per kommer ind af døren")), 'HPD REJSER SIG NR PER KOMMER IND AF DREN')

        self.assertEqual(cesar.crypt(-40, cesar.crypt(40, "H5PD rejser sig, når Per kommer ind af døren")), 'HPD REJSER SIG NR PER KOMMER IND AF DREN')

    # TODO Kevin: test_decrupt_nostrip(self):

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)


if __name__ == '__main__':
    unittest.main()
