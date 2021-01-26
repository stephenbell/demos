from faker import Faker
from faker.providers import internet


def demo_locale():
    fake = Faker(["it_IT", "en_US", "ja_JP"])
    print(fake.name())


def demo_providers():
    fake = Faker()
    fake.add_provider(internet)
    print(fake.ipv4_private())


def demo_basics():
    fake = Faker()
    print(fake.name())
    print(fake.address())
    print(fake.text())


def main():
    demo_basics()
    demo_locale()
    demo_providers()


if __name__ == "__main__":
    main()
