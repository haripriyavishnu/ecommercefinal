
from django.urls import path
from ecommerce_app import views

urlpatterns=[
    path('',views.login),
    path('login_post',views.login_post),
    path('adminpage',views.adminpage),
    path('deliverypage',views.deliverypage),
    path('shoppage',views.shoppage),
    path('userpage',views.userpage),
    path('logout',views.logout),
    path('view_user',views.view_user),
    path('view_user_search',views.view_user_search),
    path('view_shop',views.view_shop),
    path('view_shop_search',views.view_shop_search),
    path('approve_shop/<id>',views.approve_shop),
    path('reject_shop/<id>',views.reject_shop),
    path('add_changepassword_admin',views.add_changepassword_admin),
    path('add_changepassword_admin_POST',views.add_changepassword_admin_POST),
    path('manage_shop_admin',views.manage_shop_admin),
    path('view_complaint_admin',views.view_complaint_admin),
    path('sent_reply_admin/<id>',views.sent_reply_admin),
    path('sent_reply_admin_post',views.sent_reply_admin_post),
    path('view_feedback_admin',views.view_feedback_admin),
    path('shopcategory',views.shopcategory),
    path('shopcategory_POST',views.shopcategory_POST),
    path('edit_shopcategory/<id>',views.edit_shopcategory),
    path('edit_shopcategory_POST',views.edit_shopcategory_POST),
    path('view_shopcategory',views.view_shopcategory),
    path('view_shopcategory_search',views.view_shopcategory_search),
    path('delete_shopcategory/<id>',views.delete_shopcategory),
    path('add_shop',views.add_shop),
    path('add_shop_POST',views.add_shop_POST),
    path('view_profile_shop',views.view_profile_shop),
    path('edit_profile_shop',views.edit_profile_shop),
    path('edit_view_profile_shop_POST',views.edit_view_profile_shop_POST),
    path('add_product_shop',views.add_product_shop),
    path('add_product_shop_POST',views.add_product_shop_POST),
    path('view_product_shop',views.view_product_shop),
    path('view_product_shop_search',views.view_product_shop_search),

    path('view_product_user',views.view_product_user),
    path('view_product_user_search',views.view_product_user_search),

    path('delete_product_shop/<id>',views.delete_product_shop),
    path('edit_product_shop/<id>',views.edit_product_shop),
    path('edit_product_shop_POST',views.edit_product_shop_POST),
    path('view_order',views.view_order),
    path('view_order_search',views.view_order_search),
    path('add_delivery',views.add_delivery),
    path('add_delivery_POST',views.add_delivery_POST),
    path('edit_delivery/<id>',views.edit_delivery),
    path('edit_delivery_POST',views.edit_delivery_POST),
    path('delete_delivery/<id>',views.delete_delivery),
    path('view_delivery',views.view_delivery),
    path('view_delivery_search',views.view_delivery_search),
    path('add_changepassword_shop',views.add_changepassword_shop),
    path('add_changepassword_shop_POST',views.add_changepassword_shop_POST),
    path('view_rating',views.view_rating),
    path('add_user',views.add_user),
    path('add_user_POST',views.add_user_POST),
    path('edit_profile_user/<id>',views.edit_profile_user),
    path('edit_profile_user_POST',views.edit_profile_user_POST),
    path('view_profile_user',views.view_profile_user),
    path('sent_complaint_user',views.sent_complaint_user),
    path('sent_complaint_user_POST',views.sent_complaint_user_POST),
    path('assignorder/<id>',views.assignorder),
    path('assignorder_POST',views.assignorder_POST),
    path('add_changepassword_user',views.add_changepassword_user),
    path('add_changepassword_user_POST',views.add_changepassword_user_POST),
    path('add_cart/<id>',views.add_cart),
    path('add_cart_POST',views.add_cart_POST),
    path('sent_feedback_user',views.sent_feedback_user),
    path('sent_feedback_POST',views.sent_feedback_POST),
    path('order_product_user/<id>',views.order_product_user),
    path('order_product_user_POST/<id>',views.order_product_user_POST),
    path('view_cart',views.view_cart),
    path('view_cart_search',views.view_cart_search),
    path('sent_rating_user/<id>',views.sent_rating_user),
    path('sent_rating_user_POST',views.sent_rating_user_POST),
    path('view_profile_delivery',views.view_profile_delivery),
    path('view_assign_order',views.view_assign_order),
    path('view_assign_order_search',views.view_assign_order_search),
    path('view_order_user',views.view_order_user),
    path('assignorder_user/<id>',views.assignorder_user),
    path('assignorder_POST_user',views.assignorder_POST_user),
    path('view_assign_order_user',views.view_assign_order_user),
    path('update_order/<id>',views.update_order),
    path('view_reply_user/',views.view_reply_user),




















]