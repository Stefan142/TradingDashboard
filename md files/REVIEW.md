# Studenten waarmee ik heb samengewerkt. 
1. Max Hoogeveen
2. Leo Zinn
***
# Verbeterpunten die terugkwamen in beide reviews

1. Op verschillende HTML pagina's waar de user nog al is ingelogd staat de optie dat iemand kan registreren als diegene dat wil. Dit is echter niet nodig omdat de persoon al ingelogd is dus deze opties moeten weg.
   
2. Er staan nog imports genoteerd die nergens in de code gebruikt worden dus die zou ik weg moeten halen.
   
3. Voor mijn simulatie gebruik ik een csv file die gemaakt is door het lezen van een json response. Max had mij verteld dat dit ook zonder de csv file kon en direct met de JSON reponse. Dus dat ik een omweg neem naar hetzelfde resultaat.
   
4. De volgende keer een bootstrap zoeken die een directe link verschaft inplaats van een css file. Dit zorgt ervoor dat ik niet per ongeluk de bootstrap css aanpas waardoor het later meer onoverzichtelijk is wat ik zelf heb toegevoegd en aangepast heb ten opzichte met wat standaard erin zat.
   
5. Consistentie van stijl, zoals tabs spaties etc.
   
6. Comments toevoegen omdat er haast geen aanwezig zijn.
   
7. De sidebalk hoeft niet aanwezig te zijn bij het inloggen of registreren
   
8. Veel files die niet gebruikt worden of waar code in staat die niet gebruikt worden.
   
9.  Naamgeving op bepaalde plekken zou wat beter kunnen.
***
# Hoe zou ik het kunnen verbeteren?

1. Dit is eenvoudig, ik zou de HTML pagina's kunnen doorlopen en de relevante stukjes kunnen verwijderen.
   
2. simpelweg met ctlr f kijken welke functies ik gebruik en welke niet en vervolgens degene die ik niet gebruik verwijderen uit mijn import lijst.
   
3. Dit zou wat lastiger zijn om snel te implementeren lijkt me want ik moet op een of andere manier in dat geval dan iets vanuit mijn app.py direct naar mijn javascript moeten sturen. Ik zou die JSON als string kunnen opslaan als ik hem roep en dan met een hidden input naar mijn html kunnen sturen, en voordat chart word gemaakt, die response te roepen met een hidden input waar ik de value gelijk stel aan die JSON. Eigenlijk hetzelfde als de snelheid van mijn simulatie. (de gedeeltes waar ik met comments refereer naar Discchord van reddit.) Dit zou ik dan vervolgens moeten implementeren met een javascript code die hierop lijkt: (var test = document.querySelector('#my_variable').value)  eenmaal verkregen in de javascript zou ik de json daar verder moeten hendelen.
   
4. Helaas verschaft de instantie waar ik mijn bootstrap template vandaan heb gehaald geen directe link naar de css, maar gewoon een css file. Om dit te implementeren zou ik dus een andere css pagina moeten vinden wat goed met mijn html zou werken. Verder zou ik namen van classes moeten aanpassen etc. Hierom zou het sneller zijn om simpelweg een andere template te nemen van een bron die wel een link verschaft.
   
5. Simpelweg door de code lopen en kijken wat de conventie is en consistent nalopen.
   
6. Comments toevoegen bij stukjes code waar zaken nogal opstapelen en het wat lastiger kan worden.
   
7. Dit kan gedaan worden door op plekken {% if session["user_id"] %} toe te voegen waar de sidebalk word gemaakt. Dit zou het probleem moeten oplossen.
   
8. Nalopen welke er daadwerkelijk gebruikt worden en degene die niet gebruikt worden verwijderen.
   
9.  Kijken wat de variabele en/of methode/functie doet en aanpassen naar wat het doet.
***
# afwegingen
Ik wil alles implementeren, behalve 3 en 4. Simpelweg omdat er niet genoeg tijd is. Verder zijn de verbeterpunten die genoemd zijn alleen maar positief omdat ze bijdragen aan de duidelijkheid en afwerking van het project. Alles zou dus ge-ïmplementeerd moeten worden.
***
# Voorbeelden 
1. Ik heb weleens stukken code voor forms die ik schreef gekopieerd en die had ik niet verwijderd. Bijvoorbeeld dit stukje code:<br><br>
&lt;div class="card-footer text-center py-3"&gt;
  &lt;div class="small"&gt;&lt;a href="register"&gt;
  Need an account? Sign up!&lt;/a&gt;&lt;/div&gt;
&lt;/div&gt; <br><br>
Stond in verschillende html's waar je al ingelogd stond dus die kon ik simpelweg verwijderen.

1. in het begin van mijn project heb ik van finance de imports gekopieerd waardoor ik dit nog in mijn app.py heb staan. (from helpers import login_required, lookup, usd, handle_newsAPI) ik gebruik zelf nog wel helpers.py, maar lookup en bijvoorbeeld usd niet.

2. Dit stukje verbeter ik niet en is makkelijk terug te vinden in mijn code onder route simulation. Daar zie je dat ik een csv file schrijf. Dit stukje code had dus anders gekund zoals eerder beschreven.

3. Ik heb een styles.css van 10000 regels waar alle bootstrap 5 stijl elementen in verwerkd zitten.

4. Spreekt voor zich.

5. Spreekt voor zich.

6. in mijn layout kan ik erop conditioneren met de if statement of er uberhaubt een sidebalk geplaatst moet worden. Dit zit in mijn layout kan dus daar toegepast worden.

7. Aan het begin van mijn project heb ik een bootstraptemplate geimporteerd, maar hier refereer ik helemaal niet naar tijdens mijn project zoals: password.html,401.html etcetera. Hierom kan ik die simpelweg verwijderen. Ook in mijn layout staan zaken die toch aangepast worden bij het extenden, dus die kunnen ook weggelaten worden.

8. index.js, index.html veranderen naar chart.js en dashboard.html etcetera.
***