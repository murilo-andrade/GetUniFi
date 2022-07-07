from playwright.sync_api import sync_playwright
import urllib.request
import timeit

t1 = timeit.default_timer()
with open('versaoatual.txt', 'r') as file:
    atual = file.read().rstrip()
    # versao = atual
    print(f"Versão atual: {atual}")

url = "https://www.ui.com/download/unifi/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)
    info = page.locator('xpath=//*[@id="downloads"]/div[2]/div[4]/div/main/table/tbody[3]/tr[2]/td[2]').inner_text()
    versao = info.split()[3]
    print(f"Versao disponível: {versao}")
    browser.close()

if atual != versao:
    print("Baixando versão nova")
    inicio = timeit.default_timer()

    urllib.request.urlretrieve(
        f"http://www.ubnt.com/downloads/unifi/{versao}/UniFi.unix.zip", filename=f"UniFi-{versao}.unix.zip")
    urllib.request.urlretrieve(
        f"https://dl.ui.com/unifi/{versao}/unifi_sysvinit_all.deb", filename=f"unifi_sysvinit_all-{versao}.deb")
    with open('versaoatual.txt', 'w') as file:
        file.write(versao)
    final = timeit.default_timer()
    print(f"Baixado em {final - inicio} segundos")
else:
    print("Nenhuma versão nova")

t2 = timeit.default_timer()
print(f"Finalizado em {t2 - t1} segundos")
