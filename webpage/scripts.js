document.addEventListener('DOMContentLoaded', function() {
const timelineData = [
    {
        date: 'Sep 2021 - Jul 2023',
        title: 'Software Developer',
        description: '<place holder>'
    },
    {
        date: 'Aug 2021 - Jul 2023',
        title: 'Resident IoT Consultant',
        description: '<placeholder>'
    },
    {
        date: 'Apr 2021 - Aug 2021',
        title: 'Embedded Systems IoT Consultant',
        description: '<placeholder>'
    },
    {
        date: 'Jan 2021 - March 2021',
        title: 'Embedded Systems Contractor',
        description: '<placeholder>'
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
