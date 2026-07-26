import pytest

from wallet import Wallet, InsufficientAmount

# a newly created wallet has a balance of 0 by default.
def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

# a newly created wallet with an initial balance of 100 has a balance of 100.
def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

# a wallet created with an initial balance of 10 to which 90 is added has a balance of 100.
def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

# a wallet created with an initial balance of 20 from which 10 is removed has a balance of 10.
def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

# a wallet that tries to spend more than its balance will cause an InsufficientAmount error message.
def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(20)

# parametrised test using fixtures to test multiple scenarios of adding and spending cash in the wallet.
@pytest.mark.parametrize("earned,spent,expected", [(30, 10, 20), (20, 2, 18)])
def test_transactions(earned, spent, expected, empty_wallet):
    empty_wallet.add_cash(earned)
    empty_wallet.spend_cash(spent)
    assert empty_wallet.balance == expected

@pytest.fixture
def empty_wallet():
    '''Returns a wallet instance with a balance of 0.'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a wallet instance with a balance of 20.'''
    return Wallet(20)