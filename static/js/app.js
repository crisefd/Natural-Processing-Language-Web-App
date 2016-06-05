(function() {
    var app = angular.module("freelingApp", ["ngRoute", "ui.bootstrap"]);
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });
    app.controller("MainController", ["$http", "$scope",
        function($http, $scope) {
            $scope.inputText = "";
            $scope.data = [];
            $scope.isThereAnyData = function() {

                if ($scope.data.length == 0) {
                    console.log("isThereAnyData false");
                    return false;
                }
                console.log("isThereAnyData true");
                return true;
            };

            $scope.showEaglesDetails = function(eagleCode) {
							
            };
            $scope.submitText = function() {
                $scope.data = [];
                console.log("input text = " + $scope.inputText);
                console.log("sending request to server ");
                $http({
                    method: "POST",
                    url: "http://localhost:8000/morpho_analysis/",
                    data: "text=" + $scope.inputText,
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
                    }
                }).success(function(response) {
                    console.log('success');
                    $scope.data = response.data;
                    //console.log($scope.data.length)
                    console.log("data= " + $scope.data);
                }).error(function(error) {
                    console.log('error');
                });
            };
        }
    ]);

})();
