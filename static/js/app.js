(function() {
    var app = angular.module("freelingApp", ["ngRoute", "ui.bootstrap"]);
    app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });
    app.controller("MainController", ["$http", "$scope", "$uibModal", "$log",

        function($http, $scope, $uibModal, $log) {


            $scope.inputText = "";
            $scope.modalMsg = "Message";
            $scope.data = [];
            $scope.isThereAnyData = function() {

                if ($scope.data.length == 0) {
                    console.log("isThereAnyData false");
                    return false;
                }
                console.log("isThereAnyData true");
                return true;
            };

            var tagToWord = function(category, tag){
              var adjetivoDic = {
                Q: "Calificativo",
                O: "Ordinal",
                A: "Aumentativo",
                D: "Diminutivo",
                C: "Comparativo",
                S: "Superlativo",
                M: "Masculino",
                F: "Femenino",
                C:
              }
            }

            var eaglesAnalysis = function(tag){
              var analysis = "";
              switch (tag[0]) {
                case "A":
                analysis += "Adjetivo\n"
                for(var i = 1; i < tag.length; i++){
                  switch (i) {
                    case 1:
                      switch (tag[i]) {
                        case "Q": analysis += "Calificativo\n";
                          break;
                        case "O": analysis += "Ordinal\n";
                          break;
                      };
                      break;
                    case 2:
                      switch (tag[i]) {
                        case "A":
                          analysis += "Aumentativo\n";
                        break;
                        case "D":
                          analysis += "Diminutivo\n";
                          break;
                        case "C":
                          analysis += "Comparativo\n";
                          break;

                        case "S":
                          analysis += "Superlativo\n";
                          break
                      }
                    break;
                    case 3:
                      switch (tag[i]) {
                        case "M":
                          analysis += "Masculino\n";
                          break;
                        case "F":
                          analysis += "Femenino\n";
                        break;
                        case "C":
                          analysis += "Comun\n";
                        break;
                      }
                    break;

                  }

                };
                break; // adjetivo
                case "R": break;//adverbio
                case "D": break; // determinante
                case "N": break; // nombre
                case "V": break; // verbo
                case "P": break; // pronombre
                case "C": break; // conjuncion
                case "I": break; // inserjeccion
                case "S": break;//preposition
                case "F": break; //puntuacion
                case "Z": break; //numerales
                case "W": break; //fechas y horas
              }
            };

            $scope.showEagleDetails = function(eagleCode) {
                // eagle mapping here
                console.log(eagleCode);
                $scope.eagleModal = $uibModal.open({
                    template: '<div class="modal-header" ng-mouseleave="close()"><h3 class="modal-title">Message</h3></div><div class="modal-body">{[{message}]}</div><div class="modal-footer" ng-click="close()">Close</div>',
                    controller: 'modalController',
                    resolve: {
                        message: function() {
                            return $scope.modalMsg;
                        }
                    }
                });
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

    app.controller('modalController', ['$uibModalInstance', '$scope', '$log', 'message',

        function($uibModalInstance, $scope, $log, message) {
            $log.info(message);
            $scope.message = message;
            $scope.close = function() {
                $uibModalInstance.close();
            }
        }
    ]);

})();
