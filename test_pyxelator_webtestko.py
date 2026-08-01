from playwright.sync_api import sync_playwright, expect
from pyxelator import find, click, fill 
import pytest
import time
import allure


@allure.title("Pyxelator featuring Kelas-Otomesyen Test App")
@allure.description("Test ini untuk melakukan login dan menambah produk dengan Pyxelator")
@allure.severity(allure.severity_level.CRITICAL)
def test_pyxelator_ft_test_ko():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 1024})
        page = context.new_page()
        ss = page.screenshot()
        with allure.step("Navigasi ke halaman utama Kelas Otomesyen Test App"):
            page.goto("https://test.kelasotomesyen.com")

        
        with allure.step("Mengisi email"):
            fill(page, 'ss/email.png', 'uno.testing3@gmail.com')
        with allure.step("Mengisi password"):
            fill(page, 'ss/password.png', '1234567890')
        with allure.step("Klik tombol masuk"):
            click(page,'ss/masuk.png')
        expect(page.locator("//h2[@class='section-title']")).to_have_text("Semua Produk")
        page.screenshot(path="ss/after_login.png")
        assert page.url == "https://test.kelasotomesyen.com/products"

        with allure.step("Menambah produk baru"):
            click(page, 'ss/tambah_produk.png')
        with allure.step("Menambah nama produk"):
            fill(page, 'ss/nama_produk.png', 'kerbau emas')
        with allure.step("Menambah harga produk"):
            fill(page, 'ss/harga.png', '70000')
        with allure.step("Menambah stok produk"):
            fill(page, 'ss/stok.png', '17')
        with allure.step("Memilih kategori produk"):
            page.get_by_test_id("product-category-input").select_option("Home")
        with allure.step("Menambah deskripsi produk"):
            page.get_by_test_id("product-description-input").fill("kerbau emas masih menang lawan kerbau merah")
        time.sleep(3)
        allure.attach(page.screenshot(path="ss/screenshot_sebelum_submit_produk.png"), name="screenshot_sebelum_submit_produk", attachment_type=allure.attachment_type.PNG)
        # page.screenshot(path="ss/after_filling_product_details.png")
        click(page, 'ss/submit_produk.png')

        expect(page.locator("(//span[@class='product-name'])[1]")).to_have_text("kerbau emas")
        time.sleep(3)
        allure.attach(page.screenshot(path="ss/screenshot_sesudah_submit_produk.png"), name="screenshot_sesudah_submit_produk", attachment_type=allure.attachment_type.PNG)

        # time.sleep(10)
        browser.close()
