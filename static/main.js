Highcharts.chart('container1', {
    data: {
        table: 'datatable1'

    },
    chart: {
        type: 'column'
    },
    title: {
        text: 'Voters by County'
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Amount'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
        }
    }
});

Highcharts.chart('container2', {
    data: {
        table: 'datatableage'

    },
    chart: {
        type: 'column'
    },
    title: {
        text: 'Voters by Age'
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Amount'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
        }
    }
});

Highcharts.chart('container3', {
    data: {
        table: 'datatablegender'

    },
    chart: {
        type: 'column'
    },
    title: {
        text: 'Voters by Gender'
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Amount'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
        }
    }
});

Highcharts.chart('container4', {
    data: {
        table: 'datatablerace'

    },
    chart: {
        type: 'column'
    },
    title: {
        text: 'Voters by Race'
    },
    xAxis: {
        type: 'category'
    },
    yAxis: {
        allowDecimals: false,
        title: {
            text: 'Amount'
        }
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                this.point.y + ' ' + this.point.name.toLowerCase();
        }
    }
});


var mySwiper = new Swiper('.swiper-container', {
  loop: true,
  autoplay: {
    delay: 5000
  },
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});
