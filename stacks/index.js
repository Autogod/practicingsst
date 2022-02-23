import storagestack from "./storagestack.py"
import ApiStack from "./Apistacks";

export default function main(app) {
  // Set default runtime for all functions
  new StorageStack(app, "storage")
  // Add more stacks
}
