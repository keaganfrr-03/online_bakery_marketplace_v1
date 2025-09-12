from django.contrib import admin
from django.urls import path, include
from web_app.views import (
    index, category_detail, CustomLoginView, add_to_cart, cart_view, remove_from_cart, checkout_view,
    order_confirmation, register_view, vendor_dash, add_product, edit_product, delete_product, profile_view,
    profile_edit, invoice_view)
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),

    # DRF routers for APIs
    path("api/", include("web_app.urls")),

    # Pages
    path("", index, name="index"),
    path("category/<int:category_id>/", category_detail, name="category_detail"),
    path("about/", lambda request: render(request, "about.html"), name="about"),
    path("contact/", lambda request: render(request, "contact.html"), name="contact"),

    # Auth
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page="index"), name="logout"),
    path("accounts/register/", register_view, name="register"),
    path("accounts/profile/", profile_view, name="profile"),
    path("accounts/profile/edit/", profile_edit, name="profile_edit"),
    path("accounts/profile/invoice/<int:order_id>/", invoice_view, name="invoice"),


    # Cart handling
    path("cart/", cart_view, name="cart"),
    path("cart/add-auth/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:product_id>/", remove_from_cart, name="cart_remove"),
    path("checkout/", checkout_view, name="checkout"),
    path("order/<int:order_id>/confirmation/", order_confirmation, name="order_confirmation"),

    # Vendor Dashboard
    path("vendor_dash/", vendor_dash, name="vendor_dash"),
    path("vendor/add/", add_product, name="add_product"),
    path("vendor/edit/<int:product_id>/", edit_product, name="edit_product"),
    path("vendor/delete/<int:product_id>/", delete_product, name="delete_product"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
