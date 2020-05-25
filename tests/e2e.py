import pytest
import selfies as sf


class EndToEndTestCase:
    def __init__(self, identifier: str, smiles: str, selfies: str = None):
        self.identifier = identifier
        self.smiles = smiles
        self.selfies = selfies


test_cases = [
    EndToEndTestCase(
        identifier='Pentylamine',
        smiles='CCCCCN',
        selfies='[C][C][C][C][C][N]'
    ),
    EndToEndTestCase(
        identifier='Phenylalanine',
        smiles='N[C@@H](CC1=CC=CC=C1)C(O)=O',
    ),
    EndToEndTestCase(
        identifier='MDMA',
        smiles='CC(CC1=CC2=C(C=C1)OCO2)NC',
    ),
    EndToEndTestCase(
        identifier='DEET',
        smiles='O=C(c1cc(ccc1)C)N(CC)CC',
    ),
    EndToEndTestCase(
        identifier='Paracetamol',
        smiles='CC(=O)Nc1ccc(O)cc1',
    ),
    EndToEndTestCase(
        identifier='Ibuprofen',
        smiles='CC(C)CC1=CC=C(C=C1)C(C)C(=O)O',
    ),
    EndToEndTestCase(
        identifier='Afatinib',
        smiles='CN(C)CC=CC(=O)NC1=C(C=C2C(=C1)C(=NC=N2)NC3=CC(=C(C=C3)F)Cl)OC4CCOC4',
    ),
    EndToEndTestCase(
        identifier='Sorafenib',
        smiles='CNC(=O)C1=NC=CC(=C1)OC2=CC=C(C=C2)NC(=O)NC3=CC(=C(C=C3)Cl)C(F)(F)F',
    ),
    EndToEndTestCase(
        identifier='Azulene',
        smiles='C1=CC=C2C=CC=C2C=C1',
    ),
    EndToEndTestCase(
        identifier='Chrysene',
        smiles='C1=CC=C2C(=C1)C=CC3=C2C=CC4=CC=CC=C43',
    )
]


@pytest.mark.parametrize("case", test_cases, ids=[tc.identifier for tc in test_cases])
def test_smiles_to_selfies(case: EndToEndTestCase):
    if not case.selfies:
        pytest.skip('Need to add an expected SELFIES result for this molecule!')
    assert sf.encoder(case.smiles) == case.selfies


@pytest.mark.parametrize("case", test_cases, ids=[tc.identifier for tc in test_cases])
def test_roundtrip_smiles_to_selfies(case: EndToEndTestCase):
    output_selfies = sf.encoder(case.smiles)
    roundtrip_smiles = sf.decoder(output_selfies)
    assert case.smiles == roundtrip_smiles
