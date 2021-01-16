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
    view.backgroundColor = .systemBackground

    let groceryMainViewController = GroceryMainViewController()
    let navigationController = UINavigationController(rootViewController: groceryMainViewController)

    navigationController.willMove(toParent: self)
    view.addSubview(navigationController.view)
    addChild(navigationController)
    navigationController.didMove(toParent: self)
  }
}

struct GroceryItem: Hashable {
  let id: String
  let name: String
  let createdBy: String
  let createdAt: Date
  let editedBy: String
  let editedAt: Date
}

func createTestGroceryItem(name: String, creator: String = "milan") -> GroceryItem {
  return GroceryItem(id: UUID().uuidString, name: name, createdBy: creator, createdAt: Date(), editedBy: creator, editedAt: Date())
}

let sampleDataItems: [GroceryItem] = [
  createTestGroceryItem(name: "Milk"),
  createTestGroceryItem(name: "Cheese"),
  createTestGroceryItem(name: "Eggs"),
]

class GroceryMainViewController: UIViewController {
  enum Section {
    case main
  }

  var dataSource: UICollectionViewDiffableDataSource<Section, GroceryItem>!

  override func viewDidLoad() {
    super.viewDidLoad()
    view.backgroundColor = .systemBackground

    let collectionViewLayoutConfiguration = UICollectionLayoutListConfiguration.init(appearance: .plain)
    let collectionViewLayout = UICollectionViewCompositionalLayout.list(using: collectionViewLayoutConfiguration)
    let collectionView = UICollectionView(frame: .zero, collectionViewLayout: collectionViewLayout)
    collectionView.translatesAutoresizingMaskIntoConstraints = false
    collectionView.backgroundColor = .systemBackground


    let cellRegistration = UICollectionView.CellRegistration<UICollectionViewListCell, GroceryItem> { (cell: UICollectionViewListCell, path: IndexPath, item: GroceryItem) in
      var content = cell.defaultContentConfiguration()
      content.text = item.name
      cell.contentConfiguration = content
    }

    dataSource = UICollectionViewDiffableDataSource<Section, GroceryItem>(collectionView: collectionView) { (collectionView: UICollectionView, indexPath: IndexPath, item: GroceryItem) in
      let cell = collectionView.dequeueConfiguredReusableCell(using: cellRegistration, for: indexPath, item: item)
      cell.accessories = [.disclosureIndicator()]
      return cell
    }

    var initialSnapshot = NSDiffableDataSourceSnapshot<Section, GroceryItem>()
    initialSnapshot.appendSections([.main])
    initialSnapshot.appendItems(sampleDataItems, toSection: .main)
    dataSource.apply(initialSnapshot, animatingDifferences: false)

    view.addSubview(collectionView)
    NSLayoutConstraint.activate([
      collectionView.leftAnchor.constraint(equalTo: view.safeAreaLayoutGuide.leftAnchor),
      collectionView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
      collectionView.trailingAnchor.constraint(equalTo: view.safeAreaLayoutGuide.trailingAnchor),
      collectionView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
    ])
  }
}

