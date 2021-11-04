import React from "react";
import { Link } from "react-router-dom";

import PlusIcon from "../../assets/images/plus.svg";

export default function CategoryCard(props) {
	const { id, name, image } = props.data;
	return (
		<Link to={`/?category=${id}`}>
			<div className="category-items">
				<img className="category-image" src={image} alt="" />
				<div className="white-transparent"></div>
				<img className="category-plus" src={PlusIcon} alt="" />
				<p className="category-text">{name}</p>
			</div>
		</Link>
	);
}
