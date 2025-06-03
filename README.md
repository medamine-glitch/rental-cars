# RentalCars - Premium Car Rental Website

A modern and feature-rich car rental website built with Django and TailwindCSS. This project provides a seamless experience for users to browse, filter, and rent cars while offering a comprehensive admin interface for managing the rental fleet.

## 🚗 Features

### For Users
- Modern, responsive design with smooth animations
- Advanced car search and filtering system
- Detailed car information and specifications
- User reviews and ratings
- Contact form with validation
- Interactive location map
- Testimonials section
- About us page with company timeline
- Mobile-friendly interface

### For Admins
- Comprehensive admin dashboard
- Easy car management (add, edit, delete)
- Multiple image upload for cars
- Review management
- Contact message handling
- Team member management
- Partner/Brand management
- Analytics and statistics

## 🛠️ Technologies Used

- **Backend**: Django 5.0.2
- **Frontend**: TailwindCSS, Alpine.js
- **Database**: SQLite (default) / PostgreSQL (recommended for production)
- **Image Handling**: Pillow
- **Forms**: django-crispy-forms
- **Animations**: AOS (Animate on Scroll)
- **Icons**: Heroicons
- **Maps**: Google Maps API

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rental-cars.git
   cd rental-cars
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create environment variables file (.env):
   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key
   ```

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/admin` to access the admin interface and start adding content.

## 📁 Project Structure

```
rental-cars/
├── cars/                   # Main app directory
│   ├── migrations/        # Database migrations
│   ├── static/           # Static files (CSS, JS, images)
│   ├── templates/        # HTML templates
│   ├── admin.py         # Admin interface configuration
│   ├── models.py        # Database models
│   ├── urls.py          # URL configurations
│   └── views.py         # View functions
├── media/                # User-uploaded files
├── static/              # Project-wide static files
├── templates/           # Project-wide templates
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## 🎨 Color Scheme

The website uses a professional and modern color scheme:

- Primary Color (Deep Navy Blue): `#003366`
- Secondary Color (Teal): `#4ECDC4`
- Accent Color (Coral Red): `#FF6B6B`
- Background Light Gray: `#F2F2F2`
- Text Dark Gray: `#333333`

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop computers
- Tablets
- Mobile phones

## 🔒 Security Features

- CSRF protection
- XSS prevention
- Secure file upload handling
- Admin-only access to dashboard
- Form validation
- Secure password storage

## 🚀 Performance Optimizations

- Image optimization
- Lazy loading
- Efficient database queries
- Caching implementation
- Minified static files

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For support, email support@rentalcars.com or create an issue in the repository.

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [Alpine.js](https://alpinejs.dev/)
- [AOS](https://michalsnik.github.io/aos/)
- [Heroicons](https://heroicons.com/) 