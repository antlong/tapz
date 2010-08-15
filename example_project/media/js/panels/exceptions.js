Highcharts.setOptions({
    colors: ['#2d3736', '#50B432', '#ED561B', '#DDDF00', '#24CBE5', '#64E572', '#FF9655', '#FFF263', '#6AF9C4']
});
var chart;
$(document).ready(function() {
   chart = new Highcharts.Chart({
      chart: {
         renderTo: 'container',
         defaultSeriesType: 'column'
      },
      legend: {
           enabled: false
      },
      title: {
         text: '500 Errors'
      },
      subtitle: {
         text: 'Source: WorldClimate.com'
      },
      xAxis: {
         categories: [
            'Jan', 
            'Feb', 
            'Mar', 
            'Apr', 
            'May', 
            'Jun', 
            'Jul', 
            'Aug', 
            'Sep', 
            'Oct', 
            'Nov', 
            'Dec'
         ]
      },
      yAxis: {
         min: 0,
         title: {
            text: 'Number of Errors'
         }
      },
      legend: {
         layout: 'vertical',
         backgroundColor: '#FFFFFF',
         align: 'left',
         verticalAlign: 'top',
         x: 100,
         y: 70
      },
      tooltip: {
         formatter: function() {
            return ''+
               this.x +': '+ this.y +' errors';
         }
      },
      plotOptions: {
         column: {
            pointPadding: 0.2,
            borderWidth: 0
         }
      },
           series: [{
         name: 'Errors',
         data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
   
      }]
   });
   
   
});