from langchain_mariadb import __all__

EXPECTED_ALL = [
    "__version__",
    "MariaDBChatMessageHistory",
    "MariaDBStore",
    "MariaDBTranslator",
]


def test_all_imports() -> None:
    """Test that __all__ is correctly defined."""
    assert sorted(EXPECTED_ALL) == sorted(__all__)
