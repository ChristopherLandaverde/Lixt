//
//  ViewController.swift
//  Lixt
//
//  Created by Marlon Landaverde on 1/15/21.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.

        let helloWorldLabel = UILabel()
        helloWorldLabel.translatesAutoresizingMaskIntoConstraints = false
        helloWorldLabel.text = "Hello from Lixt app"

        view.addSubview(helloWorldLabel)

        NSLayoutConstraint.activate([
            helloWorldLabel.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            helloWorldLabel.centerYAnchor.constraint(equalTo: view.centerYAnchor),
        ])
    }


}

