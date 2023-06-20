        const alerts = document.querySelectorAll('.custom-alert');
        alerts.forEach((alert) => {
            const randomColor = getRandomColor();
            alert.style.backgroundColor = randomColor;
        });

        function getRandomColor() {
            const letters = '0123456789ABCDEF';
            let color = '#';
            let attempts = 0;

            // Генерируем цвет и проверяем яркость
            while (attempts < 10) {
                color = '#';
                for (let i = 0; i < 6; i++) {
                    color += letters[Math.floor(Math.random() * 16)];
                }

                // Получаем яркость цвета
                const brightness = calculateBrightness(color);

                // Проверяем, чтобы цвет был светлым
                if (brightness > 125) {
                    return color;
                }

                attempts++;
            }

            // Если не удалось сгенерировать светлый цвет, вернем темно-серый цвет
            return '#555';
        }

        // Рассчитываем яркость цвета
        function calculateBrightness(color) {
            const hexColor = color.replace('#', '');
            const red = parseInt(hexColor.substr(0, 2), 16);
            const green = parseInt(hexColor.substr(2, 2), 16);
            const blue = parseInt(hexColor.substr(4, 2), 16);
            const brightness = (red * 299 + green * 587 + blue * 114) / 1000;
            return brightness;
        }

        const checkboxes = document.querySelectorAll('.custom-task-checkbox');
        checkboxes.forEach((checkbox) => {
            checkbox.addEventListener('change', function () {
                const taskLabel = this.nextElementSibling;
                if (this.checked) {
                    taskLabel.style.textDecoration = 'line-through';
                } else {
                    taskLabel.style.textDecoration = 'none';
                }
            });
        });
