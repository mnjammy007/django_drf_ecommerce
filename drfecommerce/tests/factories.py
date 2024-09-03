import factory

from drfecommerce.product.models import Category, Brand, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("word")


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Faker("word")


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("word")
    description = factory.Faker("sentence")
    is_digital = factory.Faker("boolean")
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
