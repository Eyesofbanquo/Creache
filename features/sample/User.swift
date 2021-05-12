struct User {
    var name: String!
    var age: Int
    var isHappy: Bool

    enum CodingKeys: String, CodingKey {
        case name, age
        case isHappy = "is_happy"
    }

    init(from decoder: Decoder) throws {
        let container = try container.decode(keyedBy: CodingKeys.self)

        name = try container.decode(String.self, forKey: .name)
        age = try container.decode(Int.self, forKey: .age)
        isHappy = try container.decode(Bool.self, forKey: .isHappy)
    }
}