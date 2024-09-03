import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    def test_get_category(self, category_factory, api_client):
        # Arrange
        category_factory.create_batch(4)
        # Act
        response = api_client().get("/api/category/")
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestBrandEndpoints:
    def test_get_brand(self, brand_factory, api_client):
        # Arrange
        brand_factory()
        # Act
        response = api_client().get("/api/brand/")
        # Assert
        assert response.status_code == 200


class TestProductEndpoints:
    def test_get_product(self, product_factory, api_client):
        # Arrange
        product_factory()
        # Act
        response = api_client().get("/api/product/")
        # Assert
        assert response.status_code == 200
