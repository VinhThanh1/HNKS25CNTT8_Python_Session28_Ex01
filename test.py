def input_float(message, minimum):
    while True:
        try:
            value = float(input(message))

            if value < minimum:
                print(f"Giá trị phải >= {minimum}")
                continue

            return value

        except:
            print("Vui lòng nhập số hợp lệ!")
    
def input_int(message, minimum, maximum):
    while True:
        try:
            value = int(input(message))

            if value < minimum or value > maximum:
                print(f"Giá trị phải từ {minimum} đến {maximum}")
                continue

            return value

        except:
            print("Vui lòng nhập số nguyên hợp lệ!")


class Product:
    def __init__(self, product_id, name, price, quantity_sold, discount):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity_sold = quantity_sold
        self.discount = discount

        self.total_revenue = 0
        self.revenue_type = ""
        self.calculate_revenue()
        self.classify_revenue()

    def calculate_revenue(self):
        revenue = self.price * self.quantity_sold - self.discount
        self.total_revenue = max(revenue, 0)
    
    def classify_revenue(self):
        revenue = self.total_revenue

        if revenue < 5_000_000:
            self.revenue_type = "Thấp"
        elif revenue < 20_000_000:
            self.revenue_type = "Trung bình"
        elif revenue < 50_000_000:
            self.revenue_type = "Khá"
        else:
            self.revenue_type = "Cao"


class ProductManager:
    def __init__(self):
        self.products = []
    
    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None
        
    def add_product(self):
        print("\n===== THÊM SẢN PHẨM =====")

        while True:
            product_id = input("Mã sản phẩm: ").strip()

            if product_id == "":
                print("Mã sản phẩm không được rỗng")
                continue

            if self.find_by_id(product_id):
                print("Mã sản phẩm đã tồn tại")
                continue
            break

        while True:
            name = input("Tên sản phẩm: ").strip()
            if name == "":
                print("Tên sản phẩm không được rỗng!")
            else:
                break
        
        price = input_float("Giá bán: ", 0)
        quantity = input_int("Số lượng bán: ", 0, 10000)
        discount = input_float("Giảm giá: ", 0)

        product = Product(product_id, name, price, quantity, discount)

        self.products.append(product)

        print("Thêm sản phẩm thành công.")
    
    def show_all(self):
        print("\n===== DANH SÁCH SẢN PHẨM =====")

        if not self.products:
            print("Danh sách sản phẩm đang rỗng")
            return
        
        print(
            f"{'Mã | '}"
            f"{'Tên sản phẩm | '}"
            f"{'Giá bán | '}"
            f"{'SL bán | '}"
            f"{'Giảm giá | '}"
            f"{'Doanh thu | '}"
            f"{'Loại'}"
        )

        for p in self.products:
            print(
                f"{p.id} | "
                f"{p.name} | "
                f"{p.price} | "
                f"{p.quantity_sold} | "
                f"{p.discount} | "
                f"{p.total_revenue} | "
                f"{p.revenue_type}"
            )

    def update_product(self):
        print("\n===== CẬP NHẬT SẢN PHẨM =====")
        product_id = input("Nhập mã sản phẩm: ").strip()

        product = self.find_by_id(product_id)

        if product is None:
            print("Không tìm thấy sản phẩm")
            return

        product.price = input_float("Giá bán mới: ", 0)
        product.quantity_sold = input_int("Số lượng bán mới: ", 0, 10000)
        product.discount = input_float("Giảm giá mới: ", 0)

        product.calculate_revenue()
        product.classify_revenue()

        print("Cập nhật sản phẩm thành công!")

    def delete_product(self):
        print("\n===== XÓA SẢN PHẨM =====")
        product_id = input("Nhập mã sản phẩm: ").strip()

        product = self.find_by_id(product_id)
        if product is None:
            print("Không tìm thấy sản phẩm")
            return

        confirm = input("Bạn có chắc muốn xóa sản phẩm này không? (Y/N): ")

        if confirm.lower() == "y":
            self.products.remove(product)
            print("Xóa sản phẩm thành công")
        elif confirm.lower() == "n":
            print("Đã hủy thao tác xóa")
        else:
            print("Lựa chọn không hợp lệ")



def show_menu():
    print("\n================ MENU ================")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("6. Thống kê doanh thu")
    print("7. Thoát")
    print("=====================================")


def load_sample_data(manager):
    manager.products.append(Product("SP001", "Laptop Dell", 15000000, 3, 2000000))
    manager.products.append(Product("SP002", "Chuột Logitech", 350000, 20, 500000))
    manager.products.append(Product("SP003", "Bàn phím cơ AKKO", 1200000, 10, 1000000))
    manager.products.append(Product("SP004", "Màn hình Samsung", 4500000, 5, 0))
    manager.products.append(Product("SP005", "Tai nghe Sony", 2500000, 1, 0))


def main():
    manager = ProductManager()

    load_sample_data(manager)

    while True:
        show_menu()

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            manager.show_all()
        elif choice == "2":
            manager.add_product()
        elif choice == "3":
            manager.update_product()
        elif choice == "4":
            manager.delete_product()
        elif choice == "7":
            print("Cảm ơn bạn đã sử dụng hệ thống quản lý sản phẩm!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()


  
    