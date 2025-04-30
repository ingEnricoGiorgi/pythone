import urllib.request

url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")
import bs4

doc = bs4.BeautifulSoup(text)
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag:
        tds = tr.contents
        #sequ = int(tds[0].get_text())
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".", ""))
        kmq = tds[4].get_text()
        sigl = tds[7].get_text()
        valoreDens = float(tds[5].get_text().replace(".", "").replace(",", "."))
        dens = round(valoreDens,1)
        calcDensTemp = float(resi / float(kmq.replace(".", "").replace(",", ".")))
        calcDens=round(calcDensTemp,1)
        if(dens != calcDens):
            message="Valore discostato"
        else:
            message="Valore corretto"    
        #print(f"{sequ:3d} {prov:25s} {resi:9d} {sigl}")
        #print(f"{'Sigla'} {'Provincia':25s} {'Residenti':9s} {'Kmq':5s} {'Dens':5s} {'CalcD':5s} {'Valutazione':15s}")


        print(f"{sigl} - {prov:25s} - {resi:9d} - {kmq:5s} - {dens:.1f} - {calcDens:.1f} - {message:15s}")
