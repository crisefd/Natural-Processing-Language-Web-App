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
            $scope.analyzer = "";


            $scope.isThereAnyData = function() {

                if ($scope.data.length == 0) {
                    console.log("isThereAnyData false");
                    return false;
                }
                console.log("isThereAnyData true");
                return true;
            };

            var eaglesAnalysis = function(tag){
              var analysis = "";
              switch (tag[0]) {
                case "A":
                analysis += "Adjetivo\n";
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
                          break;
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

                  case 4:
                    switch (tag[i]) {
                      case "S":
                        analysis += "Singular\n";
                        break;
                      case "P":
                        analysis += "Plural\n";
                        break;
                      case "N":
                        analysis += "Invariable\n";
                        break;
                    }
                  break;
                  case 5:
                    switch (tag[i]) {
                      case "0":
                        analysis += "-\n";
                        break;
                      case "P":
                        analysis += "Participio\n";
                        break;
                    }
                  break;

                  }

                };
                break; // adjetivo
                case "R":
                    analysis += "Adverbio\n";
                    if(tag[1] === "G"){
                      analysis += "General\n";
                    }else{
                      analysis += "Negativo\n";
                    }
                break;//adverbio
                case "D":
                  analysis += "Determinante\n";
                  for(var i = 1; i < tag.length; i++){
                    switch (i) {
                      case 1:
                        switch (tag[i]) {
                          case "D":
                            analysis += "Demonstrativo\n";
                            break;
                          case "P":
                            analysis += "Posesivo\n";
                            break;
                          case "T":
                            analysis += "Interrogativo\n";
                          break;
                          case "E":
                            analysis += "Exclamativo\n";
                            break;
                          case "I":
                            analysis += "Indefinido\n";
                            break;
                          case "A":
                            analysis += "Articulo\n";
                            break;
                        }
                        break;
                      case 2:
                        switch (tag[i]) {
                          case "1":
                            analysis += "Primera\n";
                            break;
                          case "2":
                            analysis += "Segunda\n";
                            break;
                          case "3":
                            analysis += "Tercera\n";
                            break;
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
                          case "N":
                            analysis += "Neutro\n";
                            break;
                        }
                      break;
                      case 4:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Singular\n";
                            break;
                          case "P":
                            analysis += "Plural\n";
                            break;
                          case "N":
                            analysis += "Invariable\n";
                            break;
                        }

                      break;
                      case 5:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Singular\n";
                            break;
                          case "P":
                            analysis += "Plural\n";
                            break;
                        }
                      break;

                    }
                  };
                break; // determinante
                case "N":
                  analysis += "Nombre\n";
                  for(var i = 1; i < tag.length; i++){
                    switch (i) {
                      case 1:
                        switch (tag[i]) {
                          case "C":
                            analysis += "Comun\n";
                            break;
                          case "P":
                            analysis += "Propio\n";
                            break;
                        }
                        break;
                      case 2:
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
                      case 3:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Singular\n";
                            break;
                          case "P":
                            analysis += "Plural\n";
                            break;
                          case "N":
                            analysis += "Invariable\n";
                          break;
                        }
                      break;
                      case 4:
                        switch (tag[i] + tag[i + 1]) {
                          case "SP":
                            analysis += "Persona\n";
                            break;
                          case "G0":
                            analysis += "Lugar\n";
                            break;
                          case "O0":
                            analysis += "Organizacion\n";
                          break;
                          case "V0":
                            analysis += "Otros\n";
                          break;
                        }
                      break;
                      case 6:
                        switch (tag[i]) {
                          case "A":
                            analysis += "Aumentativo\n";
                            break;
                          case "D":
                            analysis += "Diminutivo\n";
                            break;
                        }
                      break;
                    }
                  };
                break; // nombre
                case "V":
                  analysis += "Verbo\n";
                  for(var i = 1; i < tag.lenth; i++){
                    switch (i) {
                      case 1:
                        switch (tag[i]) {
                          case "M":
                            analysis += "Principal\n";
                            break;
                          case "A":
                            analysis += "Auxiliar\n";
                            break;
                          case "S":
                            analysis += "Semiauxiliar\n";
                          break;
                        }
                        break;
                      case 2:
                        switch (tag[i]) {
                          case "I":
                            analysis += "Indicativo\n";
                            break;
                          case "S":
                            analysis += "Subjuntivo\n";
                            break;
                          case "M":
                            analysis += "Imperativo\n";
                            break;
                          case "G":
                            analysis += "Gerundio\n";
                            break;
                          case "P":
                            analysis += "Participio\n";
                          break;
                        }
                        break;
                      case 3:
                        switch (tag[i]) {
                          case "P":
                            analysis += "Presente\n";
                            break;
                          case "I":
                            analysis += "Imperfecto\n";
                            break;
                          case "F":
                            analysis += "Futuro\n";
                            break;
                          case "C":
                            analysis += "Condicional\n";
                            break;
                          case "0":
                            analysis += "-\n";
                          break;
                        }
                        break;
                      case 4:
                        switch (tag[i]) {
                          case "1":
                            analysis += "Primera\n";
                            break;
                          case "2":
                            analysis += "Segunda\n";
                            break;
                          case "3":
                            analysis += "Tercera\n";
                            break;
                        }
                      break;
                      case 5:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Singular\n";
                            break;
                          case "P":
                            analysis += "Plural\n";
                          break;

                        }
                      break;
                      case 6:
                        switch (tag[i]) {
                          case "M":
                            analysis += "Masculino\n";
                            break;
                          case "F":
                            analysis += "Femenino\n";
                          break;

                        }
                      break;
                    }
                  };
                break; // verbo
                case "P":
                analysis += "Pronombre\n"
                  for(var i = 1; i < tag.lenth; i++){
                    switch (i) {
                      case 1:
                        switch (tag[i]) {
                          case "P":
                            analysis += "Personal\n";
                            break;
                          case "D":
                            analysis += "Demonstrativo\n";
                            break;
                          case "X":
                            analysis += "Posesivo\n";
                            break;
                          case "I":
                            analysis += "Indefinido\n";
                            break;
                          case "T":
                            analysis += "Interrogativo\n";
                            break;
                          case "R":
                            analysis += "Relativo\n";
                            break;
                          case "E":
                            analysis += "Exclamativo\n";
                            break;
                        }
                        break;
                      case 2:
                        switch (tag[i]) {
                          case "1":
                            analysis += "Primera\n";
                            break;
                          case "2":
                            analysis += "Segunda\n";
                            break;
                          case "3":
                            analysis += "Tercera\n";
                            break;
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
                          case "N":
                            analysis += "Neutro\n";
                            break;
                        }
                        break;
                      case 4:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Singular\n";
                            break;
                          case "P":
                            analysis += "Plural\n";
                            break;
                          case "N":
                            analysis += "ImpersonalMI\n";
                            break;
                        }
                      break;
                      case 5:
                        switch (tag[i]) {
                          case "N":
                            analysis += "Nominativo\n";
                            break;
                          case "A":
                            analysis += "Acusativo\n";
                            break;
                          case "D":
                            analysis += "Dativo\n";
                            break;
                          case "O":
                            analysis += "Oblicuo\n";
                            break;

                        }
                      break;
                      case 6:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Singular\n";
                            break;
                          case "P":
                            analysis += "Plural\n";
                          break;

                        }
                      break;
                      case 7:
                        analysis += "Cortez";
                      break;
                    }
                  };
                break; // pronombre
                case "C":
                  analysis += "Conjuncion\n";
                  if(tag[1] === "C"){
                    analysis += "Coordinada\n";
                  }else{
                    if(tag[1] === "S"){
                      analysis += "Subordinada\n";
                    }
                  }
                break; // conjuncion
                case "I":
                  analysis += "Interjeccion\n";
                break; // inserjeccion
                case "S":
                  analysis += "Adposicion\n";
                  for(var i = 1; i < tag.length ; i++){
                    switch (i) {
                      case 1:
                        switch (tag[i]) {
                          case "P":
                            analysis += "Preposicion\n";
                            break;
                        }
                        break;
                      case 2:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Simple\n";
                            break;
                          case "C":
                            analysis += "Contraida\n";
                            break;
                        }
                      break;
                      case 3:
                        switch (tag[i]) {
                          case "M":
                            analysis += "Masculino\n";
                            break;
                        }
                      break;
                      case 4:
                        switch (tag[i]) {
                          case "S":
                            analysis += "Singular";
                            break;
                          default:

                        }
                      break;

                    }
                  };
                break;//preposition
                case "F":
                  analysis += "Puntuacion\n";
                break; //puntuacion
                case "Z":
                  analysis += "Cifra\n";
                  switch (tag[1]) {
                    case "d":
                      analysis += "Partitivo\n";
                      break;
                    case "m":
                      analysis += "Moneda\n";
                    break;
                    case "p":
                      analysis += "Porcentaje\n";
                    break;
                    case "u":
                      analysis += "Unidad\n";
                    break;

                  }
                break; //numerales
                case "W":
                  analysis += "Fecha/Hora\n";
                break; //fechas y horas
              }
              return analysis;
            };

            $scope.showEaglesDetails = function(eaglesCode) {
                $scope.modalMsg = eaglesAnalysis(eaglesCode);
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
            $scope.submitText = function(app_name) {
                $scope.data = [];
                //console.log("input text = " + $scope.inputText);
                console.log("sending request to server " + $scope.analyzer);
                var url;
                var data;
                if(app_name === "morpho_app"){
                  url = "http://localhost:8000/get_morphological_analysis/"
                  data = $.param({ 'text': $scope.inputText })
                }else{
                  if(app_name === "syntactic_app"){
                    url = "http://localhost:8000/get_syntactic_analysis/"
                    data = $.param({ 'text': $scope.inputText, 'analyzer': $scope.analyzer})
                  }
                }
                console.log($scope.analyzer);
                $http({
                    method: "POST",
                    url: url,
                    data: data,
                    // data: "text=" + $scope.inputText,
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
