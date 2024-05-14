```python
class ProductRecord:
    def __init__(self):
        self.product_id = ""  # 10 characters
        self.product_name = ""  # 30 characters
        self.product_quantity = 0  # 8 digits
        self.product_price = 0.00  # 8 digits with 2 decimal places


class WarehouseRecord:
    def __init__(self):
        self.warehouse_id = ""  # 10 characters
        self.warehouse_name = ""  # 30 characters
        self.warehouse_location = ""  # 50 characters


class OrderRecord:
    def __init__(self):
        self.order_id = ""  # 10 characters
        self.product_id = ""  # 10 characters
        self.order_quantity = 0  # 8 digits
        self.order_date = 0  # 8 digits YYYYMMDD


# Tables
product_table = [ProductRecord() for _ in range(100)]
warehouse_table = [WarehouseRecord() for _ in range(10)]
order_table = [OrderRecord() for _ in range(1000)]

# Individual Variables
transformation_factor = 1.10
total_order_amount = 0.00
count_orders = 0

ws_date_string = ""  # 10 characters
ws_date = 0  # YYYYMMDD
ws_time = 0  # HHMMSS
ws_day = 0
ws_month = 0
ws_year = 0
ws_hour = 0
ws_minute = 0
ws_second = 0

ws_error_code = 0
ws_error_message = ""  # 100 characters
ws_exit_code = 0
ws_file_status = ""  # 2 characters
ws_eof = 'N'

ws_invalid_quantity = 'N'
ws_invalid_date = 'N'

ws_order_date = 0  # YYYYMMDD
ws_order_amount = 0.00

ws_warehouse_index = 0
ws_product_index = 0
ws_order_index = 0

ws_report_line = ""  # 100 characters

class DateStructure:
    def __init__(self):
        self.year = 0
        self.month = 0
        self.day = 0

ws_current_date = DateStructure()
ws_start_date = DateStructure()
ws_end_date = DateStructure()

ws_report_date = ""  # 10 characters
ws_report_time = ""  # 8 characters

ws_report_file_name = ""  # 50 characters

ws_order_total = 0.00

ws_quantity_string = ""  # 8 characters

ws_order_quantity = 0
ws_quantity_display = ""

ws_temp_product_id = ""  # 10 characters
ws_temp_warehouse_id = ""  # 10 characters

ws_warehouse_found = 'N'
ws_product_found = 'N'

ws_invalid_amount = 'N'

ws_warehouse_index2 = 0
ws_product_index2 = 0
ws_order_index2 = 0

ws_product_quantity = 0
ws_product_price = 0.00
ws_acc_quantity = 0
ws_acc_price = 0.00
ws_acc_total = 0.00

ws_warehouse_index3 = 0
ws_product_index3 = 0
ws_order_index3 = 0

ws_order_amount3 = 0.00
ws_order_quantity3 = 0

ws_start_dt_string = ""
ws_end_dt_string = ""

ws_report_line_count = 0

ws_space = " "
ws_space_2 = "  "
ws_space_4 = "    "
# ... and so on up to ws_space_10000000
``` 
