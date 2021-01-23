//
// Created by Marlon Landaverde on 1/15/21.
//

import Foundation
import RxSwift

private class GroceriesAPI {
  private let baseUrl: String
  private let apiVersion: String
  private let baseApiPath: String = {
    return "http://\(baseUrl)/\(apiVersion)"
  }

  init(baseUrl: String = "localhost:5000", apiVersion: String = "v1") {
    self.baseUrl = baseUrl
    self.apiVersion = apiVersion
  }
}

class GroceriesStore {
  private let api = GroceriesAPI()
  init() {
    let api = GroceriesAPI()
  }
}
