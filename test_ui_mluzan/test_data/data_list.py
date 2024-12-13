from datetime import datetime


# ---------------------------------------General-----------------------------------------------------------------------
current_datetime = datetime.now().strftime('%Y-%m-%dT%H-%M-%S-%f')[:-3]
BASE_URL = 'https://magento.softwaretestingboard.com'

# ---------------------------------------Create Account----------------------------------------------------------------
# =========================================VALID DATA==================================================================
first_name = 'Test'
last_name = 'User'
email = f'test.user+{current_datetime}@test.com'
password = 'S_Vx8mzM55G#7t8'
conf_password = 'S_Vx8mzM55G#7t8'

account_url = f'{BASE_URL}/customer/account/'
success_message = 'Thank you for registering with Main Website Store.'
# =========================================INVALID DATA================================================================
req_field_inline_error = 'This is a required field.'
invalid_pass_length = '123'
pass_inline_error_length = (
    'Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored.'
)

# ---------------------------------------Eco Friendly------------------------------------------------------------------
# =========================================VALID DATA==================================================================
sort_by_position_value = 'position'
sort_by_product_name_value = 'name'
sort_by_price_value = 'price'

sort_by_urls = {
    sort_by_position_value: f'{BASE_URL}/collections/eco-friendly.html',
    sort_by_product_name_value: f'{BASE_URL}/collections/eco-friendly.html?product_list_order=name',
    sort_by_price_value: f'{BASE_URL}/collections/eco-friendly.html?product_list_order=price'
}

limiter_12 = '12'
limiter_24 = '24'
limiter_36 = '36'
limiter_urls = {
    limiter_12: f'{BASE_URL}/collections/eco-friendly.html',
    limiter_24: f'{BASE_URL}/collections/eco-friendly.html?product_list_limit=24',
    limiter_36: f'{BASE_URL}/collections/eco-friendly.html?product_list_limit=36'
}

# =========================================INVALID DATA================================================================


# ---------------------------------------Sale--------------------------------------------------------------------------
# =========================================VALID DATA==================================================================
main_sale_title = 'Women’s Deals'
main_sale_text = 'Pristine prices on pants, tanks and bras.'
main_sale_button_text = 'Shop Women’s Deals'

men_sale_title = 'Men’s Bargains'
men_sale_text = 'Stretch your budget with active attire'
men_sale_link_text = 'Shop Men’s Deals'

women_sale_title = 'Luma Gear Steals'
women_sale_text = 'Your best efforts deserve a deal'
women_sale_link_text = 'Shop Luma Gear'

# =========================================INVALID DATA================================================================
