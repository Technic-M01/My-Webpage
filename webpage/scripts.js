document.addEventListener('DOMContentLoaded', function() {
const timelineData = [
    {
        date: 'Sep 2021 - Jul 2023',
        title: 'Software Developer',
        description: 'Implemented Kotlin based Android app to allow customers to control and configure local products over Bluetooth. Using Java, Python, and JavaScript, managed authentication and user data with AWS services such as, Cognito, DynamoDb, API Gateway, Lambda, IAM, App Sync, and Amplify. Furthered development of the Breezy One robot by debugging and optimizing navigation and pathfinding behavior using C++ inside a Linux environment. Successfully implemented logging events by sending ROS bag messages to ThingsBoard dashboards over MQTT.'
    },
    {
        date: 'Aug 2021 - Jul 2023',
        title: 'Resident IoT Consultant',
        description: 'Using C++ and JavaScript, developed end-to-end prototype for an IoT autonomous sensor system in support of the city of Albuquerque’s smart city initiative. Prototype included mesh network capable micro-controllers, long and short range lidar sensors, servo motors to articulate the sensor mount, and miscellaneous environmental sensors to ensure sensitive equipment was not subject to adverse conditions. Collaborated with interdisciplinary team to ensure telemetry from all prototypes was successfully published to Atlantis dashboard over MQTT.'
    },
    {
        date: 'Apr 2021 - Aug 2021',
        title: 'Embedded Systems IoT Consultant',
        description: 'Successfully implemented software and hardware solutions for a calibration device utilized in the development process of new medical diagnostic devices. Software was written in C++ and C, while the devices hardware consisted of lux sensors, load cells, flex and pressure sensors, as well as a micro-controller.'
    }
];

    const timeline = document.getElementById('timeline');

    timelineData.forEach((item, index) => {
        let entry = document.createElement('div');
        entry.classList.add('timeline-entry');
        entry.setAttribute('id', 'entry-' + index);

        let dot = document.createElement('div');
        dot.classList.add('timeline-dot');

        let date = document.createElement('div');
        date.textContent = item.date;
        date.classList.add('timeline-date');

        let content = document.createElement('div');
        content.classList.add('timeline-content');
        content.setAttribute('id', 'content-' + index);

        let title = document.createElement('h3');
        title.textContent = item.title;

        let description = document.createElement('p');
        description.textContent = item.description;
        description.style.display = 'none'; // Initially hide the description

        // Click event to toggle the description visibility
        entry.addEventListener('click', function() {
            description.style.display = description.style.display === 'none' ? 'block' : 'none';
        });

        content.appendChild(title);
        content.appendChild(description);

        entry.appendChild(dot);
        entry.appendChild(date);
        entry.appendChild(content);

        timeline.appendChild(entry);
    });
});
