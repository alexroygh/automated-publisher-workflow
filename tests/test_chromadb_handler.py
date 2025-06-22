from versioning.chromadb_handler import store_version, search_version
from unittest.mock import patch, MagicMock

def test_store_version_success():
    with patch("versioning.chromadb_handler.collection.add") as mock_add:
        store_version("text", {"id": "1"})
        mock_add.assert_called_once()

def test_store_version_exception():
    with patch("versioning.chromadb_handler.collection.add", side_effect=Exception("fail")):
        store_version("text", {"id": "1"})  # Should not raise

def test_search_version_success():
    with patch("versioning.chromadb_handler.collection.query", return_value={"result": 1}):
        result = search_version("query")
        assert result == {"result": 1}

def test_search_version_exception():
    with patch("versioning.chromadb_handler.collection.query", side_effect=Exception("fail")):
        result = search_version("query")
        assert result == {} 