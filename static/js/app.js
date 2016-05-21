(function(){
	var app = angular.module('FreelingApp', []);
	app.controller('MFController', ['$http','$scope',function($http, $scope){
		$scope.inputText = '';
		$scope.submitText = function(){
			$http.post('morfo_analysis/', $scope.inputText)
				.then(
					function(response){
						console.log(response);
					},
					function(error){
						console.log(error);
					}
				);
		};
	}]);
})();
