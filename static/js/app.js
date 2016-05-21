(function(){
	var app = angular.module("freelingApp", ["ngRoute"]);
	app.controller("MAController", 
		["$http", "$scope",
		function($http, $scope){
			$scope.inputText = "";
			$scope.submitText = function(){
				console.log("input text = " + $scope.inputText);
				console.log("sending request to server ");
				$http({
					method: "POST",
					url: "http://localhost:8000/morpho_analysis/",
					data: "text=" + $scope.inputText,
					headers: {
					'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
					    }
				}).success(function(response){
					console.log('success' + JSON.stringify(response));
				}).error(function(error){
					console.log('error');
				});
			};
		}]);
})();
