from django.db import migrations

def create_sample_data(apps, schema_editor):
    Brand = apps.get_model('cars', 'Brand')
    Car = apps.get_model('cars', 'Car')
    TeamMember = apps.get_model('cars', 'TeamMember')
    Testimonial = apps.get_model('cars', 'Testimonial')
    Partner = apps.get_model('cars', 'Partner')

    # Create sample brands
    toyota = Brand.objects.create(
        name='Toyota',
        description='Japanese multinational automotive manufacturer'
    )
    bmw = Brand.objects.create(
        name='BMW',
        description='German luxury automobile manufacturer'
    )
    mercedes = Brand.objects.create(
        name='Mercedes-Benz',
        description='German luxury automotive brand'
    )

    # Create sample cars
    Car.objects.create(
        name='Camry',
        brand=toyota,
        year=2023,
        price_per_day=75.00,
        transmission='automatic',
        fuel_type='gasoline',
        seats=5,
        doors=4,
        engine='2.5L',
        mileage=15000,
        color='Silver',
        location='New York',
        description='Comfortable and reliable sedan perfect for family trips.',
        is_featured=True
    )

    Car.objects.create(
        name='3 Series',
        brand=bmw,
        year=2023,
        price_per_day=120.00,
        transmission='automatic',
        fuel_type='gasoline',
        seats=5,
        doors=4,
        engine='2.0L',
        mileage=8000,
        color='Black',
        location='Los Angeles',
        description='Luxury sports sedan with outstanding performance.',
        is_featured=True
    )

    # Create sample team members
    TeamMember.objects.create(
        name='John Smith',
        position='CEO',
        bio='Over 15 years of experience in the automotive industry.',
        email='john@rentalcars.com',
        order=1
    )

    TeamMember.objects.create(
        name='Sarah Johnson',
        position='Customer Service Manager',
        bio='Dedicated to providing exceptional customer experience.',
        email='sarah@rentalcars.com',
        order=2
    )

    # Create sample testimonials
    Testimonial.objects.create(
        name='Michael Brown',
        rating=5,
        comment='Excellent service and amazing cars! Will definitely rent again.',
        is_active=True
    )

    Testimonial.objects.create(
        name='Emily Davis',
        rating=5,
        comment='Very professional and helpful staff. The car was in perfect condition.',
        is_active=True
    )

    # Create sample partners
    Partner.objects.create(
        name='AutoCare Insurance',
        website='https://autocareinsurance.com',
        is_active=True
    )

    Partner.objects.create(
        name='SpeedyWash',
        website='https://speedywash.com',
        is_active=True
    )

def remove_sample_data(apps, schema_editor):
    Brand = apps.get_model('cars', 'Brand')
    Car = apps.get_model('cars', 'Car')
    TeamMember = apps.get_model('cars', 'TeamMember')
    Testimonial = apps.get_model('cars', 'Testimonial')
    Partner = apps.get_model('cars', 'Partner')

    Brand.objects.all().delete()
    Car.objects.all().delete()
    TeamMember.objects.all().delete()
    Testimonial.objects.all().delete()
    Partner.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_data, remove_sample_data),
    ] 