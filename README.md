# Creache

_A poorly named tool_

## Purpose

The goal of this tool is to convert `Swift` `struct` types into `class` types that can be used with `Realm Swift`.

Convert files formatted like this:

```swift
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
```

to this

```swift
class User_Entity {
    @dynamic var name: String! = ''
    @dynamic var age: Int! = 0
    @dynamic var isHappy: Bool! = false
}
```

### Features

- Automatically rename `struct` to `class` and append `_Entity_ to the new type
- Automatically generate a new entity file in the directy in which this script is called
- Automatically strip everything away thaat isn't a variable declaration
