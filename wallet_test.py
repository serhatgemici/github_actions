from wallet import Wallet, InsufficientAmount
import pytest


# a newly created wallet has a balance of 0 by default.
def test_wallet_default_balance():
    wallet = Wallet()
    assert wallet.balance == 0


# a newly created wallet with an initial balance of 100 has a balance of 100.
def test_wallet_initial_balance():
    wallet = Wallet(100)
    assert wallet.balance == 100


# a wallet created with an initial balance of 10 to which 90 is added has a balance of 100.
def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100


# a wallet created with an initial balance of 20 from which 10 is removed has a balance of 10.
def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10


# a wallet that tries to spend more than its balance will cause an InsufficientAmount error message.
def test_wallet_insufficient_amount():
    wallet = Wallet(10)
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(20)
