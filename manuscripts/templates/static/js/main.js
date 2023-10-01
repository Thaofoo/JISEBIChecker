const chartData = {
    labels: ["Passed", "Failed"],
    data: [80, 20],
    colors: ['#52B288', '#E95551']
}

const myChart = document.querySelector(".my-chart");
const ul = document.querySelector(".report-stats .details ul")

new Chart(myChart, {
    type: "doughnut",
    data: {
        labels: chartData.labels,
        datasets: [
            {
                label: "Report Value",
                data: chartData.data,
                backgroundColor: chartData.colors
            },
        ],
    },
    options: {
        borderWidth: 5,
        borderRadius: 2,
        hoverBorderWidth: 0,
        plugins: {
            legend: {
                display: true,
            },
        },
    },
});

const populateUl = () => {
    chartData.labels.forEach((l, i) => {
        let li = document.createElement("li");
        li.innerHTML = `${l}:<span class='percentage'>${chartData.data[i]}%</span>`;
        ul.appendChild(li);
    });
};

populateUl();