# Beslissingen

In het project heb ik twee grote beslissingen genomen.

1. Tijdens het project had ik van tradingview een paar advanched chart widgets ge-importeerd. Deze widgets waren perfect voor mijn app en hadden alle functionaliteiten die gewenst waren. Echter kon ik deze Widgets maar beperkt aanpassen gezien het feit dat de javascript door middel van een link ge-ïmporteerd werd. Toegang tot de javascript zelf was alleen te verkrijgen als zij dat gaven en ik kreeg dit niet. Hierom kon ik de simulatie niet runnen wat het hoofd idee was van mijn applicatie. Hierdoor moest ik schakelen naar een andere techniek, namelijk een die gebruik maakt van lightweight-charts. Deze github repository en javascript code, stelde het niet mogelijk om tekentools te maken en dergelijke. Wel was het open-source dus kon ik goed begrijpen hoe ik bijvoorbeeld data moest formatteren zodat mijn chart zou werken. Het origineel heb ik gehouden op mijn dashboard omdat de widgets toch handig zijn voor analyse en een fijne feature zijn. 

2. Als tweede grote verandering ben ik van nieuwsAPI veranderd en moest ik veel code aanpassen om aan de nieuwe API te voldoen. Ik was geswitched omdat de oude API maar 25 calls per dag toestond voor de gratis versie. waardoor het lastiger was om te testen. Dit was jammer omdat Deze nieuws API een relevantie score toestand als parameter in de call waardoor ik meer kon filteren op hoe gerelateerd nieuws moest zijn bij het draaien van de simulatie. De huidige nieuwsAPI had echter uitgebreidere samenvattingen.

***

# Extra aandachtspunten.

Ik wilde toch nadruk leggen op het feit dat ik zaken verplaatsbaar en aanpasbaar heb gemaakt in grote met javascript. Dit was toch lastig gezien het gebrek van ervaring met javascript die ik had, maar dat het toch gelukt was. Verder wilde ik de API class highlighten. Dit is namelijk een class die ik gebruikt heb om data op te slaan in verschillende routes en waarbij ik ook methods heb toegevoegd die redelijk knap handig kon checken of een symbol bestond of een speciale lijst bijhield en deze automatisch omzette tot een bepaalde format. Hierdoor blijven bijvoorbeeld ook instellingen die je hebt aangepast aan de charts gewaarborgd als je naar een andere route gaat en dergelijke. 





