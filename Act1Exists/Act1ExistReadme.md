# Activaitat Exist 1

1. Fes un programa amb interfície gràfica que tingui un entry, un botó i un label:
  - A Entry es podrà escriure un query XPath.
  - Quan pressionem el botó es farà la consulta a la bbdd i es mostrarà el resultat al label.
  - Si la consulta dona error s'avisarà amb un text al label.
  - Formatejar la sortida XML.

2. Utilitzant el fitxer [cd_catalog.xml](cd_catalog.xml):
  - Afegeix el fitxer a la col·lecció MP06UF3.
  - Crea les següents consultes (captura del teu programa amb el query i el resultat):
    - Mostra els títols dels CDs de Tina Turner.
    - Mostra els artistes dels CDs de la EU.
    - Mostra els artistes dels CDs que no siguin de la EU.
    - Mostra el títol concatenat amb l'any dels CDs de Andrea Bocelli.
    - Mostra els títols dels CDs anteriors a 1990.
    - Mostra els títols dels CDs de 1990 o posteriors.
    - Mostra els títols dels CDs que tinguin un preu inferior a 9 o superior a 10.
    - Mostra els títols dels CDs que tinguin un preu inferior a 10 i superior a 9.
    - Mostra els artistes dels CDs de la companyia EMI.

---
<h4>Mostra els títols dels CDs de Tina Turner</h4>

~~~
/CATALOG/CD[ARTIST='Tina Turner']/TITLE/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217892425-501b52d9-c6da-495f-be78-e9ac3ea88993.png"/>
</p>


<h4>Mostra els artistes dels CDs de la EU</h4>

~~~
/CATALOG/CD[COUNTRY='EU']/ARTIST/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217892559-4888061b-ca1c-43b0-b66a-9a98f85b42f0.png"/>
</p>


<h4>Mostra els artistes dels CDs que no siguin de la EU</h4>

~~~
/CATALOG/CD[not (COUNTRY='EU')]/ARTIST/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217893036-55517e8b-4495-488e-9128-f97b022e619f.png"/>
</p>


<h4>Mostra el títol concadenat amb l'any dels CDs de Andrea Bocelli.</h4>

~~~
concat("Titol:  ", /CATALOG/CD[ARTIST='Andrea Bocelli']/TITLE/text(), ", any: ", /CATALOG/CD[ARTIST='Andrea Bocelli']/YEAR/text())
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217893557-764f722c-f7fd-4f46-9978-038116060095.png"/>
</p>


<h4>Mostra els títols dels CDs anteriors a 1990.</h4>

~~~
/CATALOG/CD[YEAR<'1990']/TITLE/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217893703-dba95e7d-a50d-4ba6-8d51-c8d6339781e2.png"/>
</p>


<h4>Mostra els títols dels CDs de 1990 o posteriors.</h4>

~~~
/CATALOG/CD[YEAR>='1990']/TITLE/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217893840-301a1c40-233f-401e-8bcd-c5f368d949e0.png"/>
</p>


<h4>Mostra els títols dels CDs que tinguin un preu inferior a 9 o superior a 10.</h4>

~~~
/CATALOG/CD[PRICE < 9 or PRICE > 10]/TITLE/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217893935-3835ab84-0b12-40bb-9d0c-5a0635938eb6.png"/>
</p>


<h4>Mostra els títols dels CDs que tinguin un preu inferior a 10 i superior a 9</h4>

~~~
/CATALOG/CD[PRICE > 9 and PRICE < 10]/TITLE/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217894024-d3044716-0de7-40f2-b719-f67c687900d2.png"/>
</p>


<h4>Mostra els artistes dels CDs de la companyia EMI</h4>

~~~
/CATALOG/CD[COMPANY='EMI']/ARTIST/text()
~~~
<p align="center">
 <img src="https://user-images.githubusercontent.com/91154202/217894092-30271ad6-8bb1-412b-9cf9-43b28d53834f.png"/>
</p>
