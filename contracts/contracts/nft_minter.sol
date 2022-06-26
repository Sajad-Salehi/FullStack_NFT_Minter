// SPDX-Lisence-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";

contract nftMinter is ERC1155 {

    uint256 private tokenId;

    constructor() ERC1155("https://ipfs.io/ipfs/{}") {
        tokenId = 0;
    }

}