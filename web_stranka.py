def web_stranka():
    return """<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ovládanie Tanku</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f0f0f0; }
        .container { display: flex; flex-direction: column; align-items: center; width: 100%; max-width: 300px; }
        .slider-container { margin: 20px 0; width: auto; text-align: center; }
        .slider { width: auto; }
        .vertical-slider { transform: rotate(270deg); width: auto; margin: 50px 0; }
    </style>
</head>
<body>
    <div class="container">
        <div class="slider-container">
            <label for="dopredu_dozadu">Dopredu - Dozadu</label>
            <input type="range" id="dopredu_dozadu" class="slider vertical-slider" min="-1023" max="1023" value="0" oninput="updateDopreduDozadu(this.value)">
        </div>

        <div class="slider-container">
            <label for="otacanie_tanku">Doprava - Doľava</label>
            <input type="range" id="otacanie_tanku" class="slider" min="-1023" max="1023" value="0" oninput="updateOtacanieTanku(this.value)">
        </div>
        
        <div class="slider-container">
            <button onclick="shoot()">STREĽBA</button>
        </div>

        <div class="slider-container">
            <label for="otacanie_hlavy">Otáčanie hlavy</label>
            <input type="range" id="otacanie_hlavy" class="slider" min="-512" max="512" value="0" oninput="updateOtacanieHlavy(this.value)">
        </div>

        <div class="slider-container">
            <label for="predna_led_matica">Predná LED (jas)</label>
            <input type="range" id="predna_led_matica" class="slider" min="0" max="255" value="0" oninput="updateLed('front', this.value)">
        </div>

        <div class="slider-container">
            <label for="zadna_led_matica">Zadná LED (jas)</label>
            <input type="range" id="zadna_led_matica" class="slider" min="0" max="255" value="0" oninput="updateLed('rear', this.value)">
        </div>
    </div>

    <script>
        function updateOtacanieHlavy(value) {
            let smer = value > 0 ? 'right' : 'left';
            let rychlost = Math.abs(value);
            if (rychlost === 0) smer = 'stop';
            fetch(`/otacanie_hlavy?rychlost=${rychlost}&smer=${smer}`);
        }
        
        function shoot() {
            fetch(`/shoot`);
        }

        function updateOtacanieTanku(value) {
            fetch(`/otacanie_tanku?value=${value}`);
        }

        function updateDopreduDozadu(value) {
            fetch(`/dopredu_dozadu?value=${value}`);
        }

        function updateLed(led, jas) {
            fetch(`/led?led=${led}&jas=${jas}`);
        }
    </script>
</body>
</html>
"""